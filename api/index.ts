require("dotenv").config()

import Redis from "ioredis"
import Fastify from "fastify"
import FastifyCors from "@fastify/cors"

import anilist from "./routes/anilist"
import gogoanime from "./routes/gogoanime"
import mangadex from "./routes/mangadex"
import myanimelist from "./routes/myanimelist"

export const redis =
  process.env.REDIS_HOST &&
  new Redis({
    host: process.env.REDIS_HOST,
    port: Number(process.env.REDIS_PORT),
    password: process.env.REDIS_PASSWORD,
  })

export const tmdbApi = process.env.TMDB_KEY && process.env.TMDB_KEY
;(async () => {
  const PORT = Number(process.env.PORT) || 3000

  console.log(`Starting server on port ${PORT}... 🚀`)

  const fastify = Fastify({
    maxParamLength: 1000,
    logger: true,
  })

  await fastify.register(FastifyCors, {
    origin: "*",
    methods: "GET",
  })

  await fastify.register(anilist, { prefix: "/anilist" })
  await fastify.register(gogoanime, { prefix: "/gogoanime" })
  await fastify.register(myanimelist, { prefix: "/myanimelist" })
  await fastify.register(mangadex, { prefix: "/mangadex" })

  try {
    fastify.get("/", (_, rp) => {
      rp.status(200).send("Welcome to XO Anime API! 🎉")
    })
    fastify.get("*", (request, reply) => {
      reply.status(404).send({
        message: "",
        error: "page not found",
      })
    })

    fastify.listen({ port: PORT, host: "0.0.0.0" }, (e, address) => {
      if (e) throw e
      console.log(`server listening on ${address}`)
    })
  } catch (err: any) {
    fastify.log.error(err)
    process.exit(1)
  }
})()
