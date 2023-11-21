import { FastifyRequest, FastifyReply, FastifyInstance, RegisterOptions } from 'fastify';
import { MANGA } from '@consumet/extensions';

const routes = async (fastify: FastifyInstance, options: RegisterOptions) => {
  const mangadex = new MANGA.MangaDex();

  // Mangadex
  fastify.get('/', (_, rp) => {
    rp.status(200).send('XO Anime - Mangadex');
  });

  // Search
  fastify.get('/:query', async (request: FastifyRequest, reply: FastifyReply) => {
    const query = (request.params as { query: string }).query;
    const page = (request.query as { page: number }).page;
    const res = await mangadex.search(query, page);
    reply.status(200).send(res);
  });

  // Details
  fastify.get('/info/:id', async (request: FastifyRequest, reply: FastifyReply) => {
    const id = decodeURIComponent((request.params as { id: string }).id);
    try {
      const res = await mangadex
        .fetchMangaInfo(id)
        .catch((err) => reply.status(404).send({ message: err }));
      reply.status(200).send(res);
    } catch (err) {
      reply
        .status(500)
        .send({ message: 'Something went wrong. Please try again later.' });
    }
  });

  // Read
  fastify.get(
    '/read/:chapterId',
    async (request: FastifyRequest, reply: FastifyReply) => {
      const chapterId = (request.params as { chapterId: string }).chapterId;
      try {
        const res = await mangadex.fetchChapterPages(chapterId);
        reply.status(200).send(res);
      } catch (err) {
        reply
          .status(500)
          .send({ message: 'Something went wrong. Please try again later.' });
      }
    }
  );
};

export default routes;
