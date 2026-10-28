<template>
  <div class="fa-card flex flex-col p-5 h-100 overflow-hidden">
    <div class="fa-card-header">
      <div class="title">
        <h4>最近制品</h4>
        <p>打包产出与发布状态</p>
      </div>
    </div>
    <div class="flex flex-col flex-1 min-h-0">
      <div
        v-for="item in artifacts"
        :key="item.name"
        class="flex items-center justify-between gap-3 py-3 border-b border-g-300 last:border-b-0"
      >
        <div class="min-w-0">
          <p class="text-sm font-medium truncate">{{ item.name }}</p>
          <p class="mt-1 text-xs text-g-500">{{ item.version }} · {{ item.size }}</p>
          <p class="text-xs text-g-500">{{ item.arch }}</p>
        </div>
        <ElTag :type="statusType(item.status)" size="small" effect="light">{{ item.status }}</ElTag>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
type ArtifactStatus = "已发布" | "已打包" | "构建失败" | "待发布";

interface ArtifactItem {
  name: string;
  version: string;
  arch: string;
  size: string;
  status: ArtifactStatus;
}

const artifacts: ArtifactItem[] = [
  {
    name: "基础软件包",
    version: "2.4.1",
    arch: "linux-aarch64",
    size: "86 MB",
    status: "已发布",
  },
  {
    name: "工具链安装包",
    version: "3.1.0",
    arch: "x86_64",
    size: "124 MB",
    status: "已打包",
  },
  {
    name: "配置数据包",
    version: "1.8.6",
    arch: "qnx",
    size: "42 MB",
    status: "构建失败",
  },
  {
    name: "网关组件",
    version: "2.0.3",
    arch: "linux-arm",
    size: "67 MB",
    status: "待发布",
  },
];

const statusType = (status: ArtifactStatus) => {
  if (status === "已发布" || status === "已打包") return "success";
  if (status === "构建失败") return "danger";
  return "warning";
};
</script>
