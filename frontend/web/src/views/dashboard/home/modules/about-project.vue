<template>
  <div class="fa-card p-5 h-100 flex flex-col">
    <h2 class="text-2xl font-medium">工具能力</h2>
    <p class="text-g-700 mt-1">
      {{ systemName }} 管理基础软件的编译、打包、构建与发布，并在同一工作台查看工具链状态、构建结果和制品版本。
    </p>

    <div class="grid grid-cols-2 gap-3.5 mt-6">
      <div
        class="flex items-center gap-3 h-16 px-3.5 border border-g-300 rounded-lg bg-g-100"
        v-for="item in capabilities"
        :key="item.label"
      >
        <FaSvgIcon :icon="item.icon" class="text-xl text-theme shrink-0" />
        <span class="min-w-0">
          <span class="block text-sm text-g-800 font-medium leading-tight">{{ item.label }}</span>
          <span class="block mt-1 text-xs text-g-600">{{ item.desc }}</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import AppConfig from "@/config";

const systemName = AppConfig.systemInfo.name;

const capabilities = [
  { label: "软件编译", desc: "源码编译与交叉编译", icon: "ri:code-s-slash-line" },
  { label: "软件打包", desc: "组件打包、签名与归档", icon: "ri:archive-line" },
  { label: "构建发布", desc: "流水线构建与版本发布", icon: "ri:git-branch-line" },
  { label: "制品管理", desc: "构建产物与版本追溯", icon: "ri:inbox-archive-line" },
];
</script>
