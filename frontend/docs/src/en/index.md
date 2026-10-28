---
layout: home
editLink: true
lastUpdated: true

hero:
  name: "FastApiAdmin"
  text: "FastAPI + Vue3, one stack"
  tagline: Built on FastAPI + Vue3 + TypeScript, frontend and backend share types. 200+ REST endpoints out of the box, the AI Code Generator turns a table into full-stack CRUD, and Docker Compose brings the whole stack online in one command.
  image:
    src: /logo.svg
    alt: AI Code Generator — select a table, get the full CRUD
  actions:
    - theme: brand
      text: Quick Start
      link: /en/guide/start
    - theme: alt
      text: Live Demo
      link: https://service.fastapiadmin.com/web
      target: _blank

features:
  - icon: 📦
    title: Full-Stack & Ready
    details: Complete delivery — FastAPI async backend + Vue3 admin. Clone, run, and you're done. Zero extra configuration.

  - icon: ⚡
    title: High-Performance Async
    details: Native async/await in FastAPI, Pydantic auto type validation, Redis caching. Built for high concurrency from day one.

  - icon: 🤖
    title: AI Code Generator
    details: Select a database table → AI generates Controller / Service / Model / Vue pages. Routine CRUD is mostly automatic, so the team can focus on the business logic.

  - icon: 🛡️
    title: Enterprise RBAC
    details: JWT + OAuth2 authentication with menu, button, and data-level permission control. Full operation audit logging.

  - icon: 🐳
    title: One-Click Docker Deploy
    details: Docker Compose orchestration for the entire stack (Nginx + SSL included). One command to production with multi-environment config.
---

<script setup lang="ts">
import HomeSections from "../../.vitepress/components/HomeSections.vue";
</script>

<HomeSections />
