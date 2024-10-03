// https://nuxt.com/docs/api/configuration/nuxt-config

import { resolve } from "path";

export default defineNuxtConfig({
  alias: {
    '@': resolve(__dirname, '/'),
  },
  compatibilityDate: "2024-04-03",
  css: [
    "~/assets/main.scss",
  ],
  devtools: { enabled: true },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    }
  }
})
