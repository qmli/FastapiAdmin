<template>
  <div class="fa-card p-5 h-112">
    <div class="fa-card-header">
      <div class="title">
        <h4>高频构建</h4>
        <p>本周执行最多</p>
      </div>
    </div>
    <FaLineChart
      :showAxisLabel="false"
      :showAxisLine="false"
      :showSplitLine="false"
      :showAreaColor="true"
      :data="[8, 40, 82, 35, 90, 52, 35]"
      height="9rem"
    />
    <div class="mt-10 space-y-5">
      <div v-for="item in weeklyList" :key="item.title" class="flex items-center">
        <div
          class="size-10.5 flex items-center justify-center rounded-lg"
          :class="item.iconBgClass"
        >
          <FaSvgIcon :icon="item.icon" class="text-xl" />
        </div>
        <div class="ml-2.5">
          <p class="text-sm font-medium text-g-800">{{ item.title }}</p>
          <span class="text-sm text-g-600">{{ item.subtitle }}</span>
        </div>
        <div class="ml-auto px-3 py-1.5 text-sm text-center rounded" :class="item.valueBgClass">
          <span>{{ item.value }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface WeeklyItem {
  icon: string;
  title: string;
  subtitle: string;
  value: string;
  iconBgClass: string;
  valueBgClass: string;
}

/** 本周执行次数最多的构建对象 */
const weeklyList: WeeklyItem[] = [
  {
    icon: "ri:code-s-slash-line",
    title: "基础软件 BSW",
    subtitle: "linux-aarch64",
    value: "42 次",
    iconBgClass: "bg-theme/12 text-theme",
    valueBgClass: "bg-theme/12 text-theme",
  },
  {
    icon: "ri:archive-line",
    title: "工具链安装包",
    subtitle: "x86_64",
    value: "28 次",
    iconBgClass: "bg-success/12 text-success",
    valueBgClass: "bg-success/12 text-success",
  },
  {
    icon: "ri:cpu-line",
    title: "诊断协议栈",
    subtitle: "linux-arm",
    value: "19 次",
    iconBgClass: "bg-error/12 text-error",
    valueBgClass: "bg-error/12 text-error",
  },
];
</script>
