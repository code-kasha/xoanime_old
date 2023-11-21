import { Redis } from 'ioredis';
import { FastifyRequest, FastifyReply, FastifyInstance, RegisterOptions } from 'fastify';
import { META, PROVIDERS_LIST } from '@consumet/extensions';
import Anilist from '@consumet/extensions/dist/providers/meta/anilist';
import { StreamingServers } from '@consumet/extensions/dist/models';

import cache from '../../utils/cache';
import { redis } from '../../index';

const routes = async (fastify: FastifyInstance, options: RegisterOptions) => {
  // Anilist
  fastify.get('/', (_, rp) => {
    rp.status(200).send('XO Anime - Anilist');
  });

  // Search
  fastify.get('/:query', async (request: FastifyRequest, reply: FastifyReply) => {
    const anilist = generateAnilistMeta();
    const query = (request.params as { query: string }).query;
    const page = (request.query as { page: number }).page;
    const perPage = (request.query as { perPage: number }).perPage;
    const res = await anilist.search(query, page, perPage);
    reply.status(200).send(res);
  });

  // Trending
  fastify.get('/trending', async (request: FastifyRequest, reply: FastifyReply) => {
    const page = (request.query as { page: number }).page;
    const perPage = (request.query as { perPage: number }).perPage;
    const anilist = generateAnilistMeta();
    redis
      ? reply
          .status(200)
          .send(
            await cache.fetch(
              redis as Redis,
              `anilist:trending;${page};${perPage}`,
              async () => await anilist.fetchTrendingAnime(page, perPage),
              60 * 60
            )
          )
      : reply.status(200).send(await anilist.fetchTrendingAnime(page, perPage));
  });

  // Characters
  fastify.get('/character/:id', async (request: FastifyRequest, reply: FastifyReply) => {
    const id = (request.params as { id: string }).id;

    const anilist = generateAnilistMeta();
    const res = await anilist.fetchCharacterInfoById(id);

    reply.status(200).send(res);
  });

  // Popular
  fastify.get('/popular', async (request: FastifyRequest, reply: FastifyReply) => {
    const page = (request.query as { page: number }).page;
    const perPage = (request.query as { perPage: number }).perPage;
    const anilist = generateAnilistMeta();
    redis
      ? reply
          .status(200)
          .send(
            await cache.fetch(
              redis as Redis,
              `anilist:popular;${page};${perPage}`,
              async () => await anilist.fetchPopularAnime(page, perPage),
              60 * 60
            )
          )
      : reply.status(200).send(await anilist.fetchPopularAnime(page, perPage));
  });

  // Random
  fastify.get('/random-anime', async (request: FastifyRequest, reply: FastifyReply) => {
    const anilist = generateAnilistMeta();
    const res = await anilist.fetchRandomAnime().catch((err) => {
      return reply.status(404).send({ message: 'Anime not found' });
    });
    reply.status(200).send(res);
  });

  // Details
  fastify.get('/info/:id', async (request: FastifyRequest, reply: FastifyReply) => {
    const id = (request.params as { id: string }).id;
    const today = new Date();
    const dayOfWeek = today.getDay();
    const provider = (request.query as { provider?: string }).provider;
    let fetchFiller = (request.query as { fetchFiller?: string | boolean }).fetchFiller;
    let isDub = (request.query as { dub?: string | boolean }).dub;
    const locale = (request.query as { locale?: string }).locale;
    let anilist = generateAnilistMeta(provider);
    if (isDub === 'true' || isDub === '1') isDub = true;
    else isDub = false;
    if (fetchFiller === 'true' || fetchFiller === '1') fetchFiller = true;
    else fetchFiller = false;
    try {
      redis
        ? reply
            .status(200)
            .send(
              await cache.fetch(
                redis,
                `anilist:info;${id};${isDub};${fetchFiller};${anilist.provider.name.toLowerCase()}`,
                async () =>
                  anilist.fetchAnimeInfo(id, isDub as boolean, fetchFiller as boolean),
                dayOfWeek === 0 || dayOfWeek === 6 ? 60 * 120 : (60 * 60) / 2
              )
            )
        : reply
            .status(200)
            .send(
              await anilist.fetchAnimeInfo(id, isDub as boolean, fetchFiller as boolean)
            );
    } catch (err: any) {
      reply.status(500).send({ message: err.message });
    }
  });

  // Watch
  fastify.get(
    '/watch/:episodeId',
    async (request: FastifyRequest, reply: FastifyReply) => {
      const episodeId = (request.params as { episodeId: string }).episodeId;
      const provider = (request.query as { provider?: string }).provider;
      const server = (request.query as { server?: StreamingServers }).server;
      if (server && !Object.values(StreamingServers).includes(server))
        return reply.status(400).send('Invalid server');
      let anilist = generateAnilistMeta(provider);
      try {
        redis
          ? reply
              .status(200)
              .send(
                await cache.fetch(
                  redis,
                  `anilist:watch;${episodeId};${anilist.provider.name.toLowerCase()};${server}`,
                  async () => anilist.fetchEpisodeSources(episodeId, server),
                  600
                )
              )
          : reply.status(200).send(await anilist.fetchEpisodeSources(episodeId, server));
        anilist = new META.Anilist(undefined, {
          url: process.env.PROXY as string | string[],
        });
      } catch (err) {
        reply
          .status(500)
          .send({ message: 'Something went wrong. Contact developer for help.' });
      }
    }
  );
};

const generateAnilistMeta = (provider: string | undefined = undefined): Anilist => {
  if (typeof provider !== 'undefined') {
    let possibleProvider = PROVIDERS_LIST.ANIME.find(
      (p) => p.name.toLowerCase() === provider.toLocaleLowerCase()
    );
    return new META.Anilist(possibleProvider, {
      url: process.env.PROXY as string | string[],
    });
  } else {
    return new Anilist(undefined, {
      url: process.env.PROXY as string | string[],
    });
  }
};

export default routes;
