<template>
  <div class="fa-card h-100 p-5 mb-5 max-sm:mb-4">
    <div class="fa-card-header">
      <div class="title">
        <h4>生成目标</h4>
        <p>本周代码生成与计划对比</p>
      </div>
    </div>

    <FaBarChart
      class="p-5"
      height="12rem"
      :data="usageData"
      :xAxisData="weekDays"
      :showAxisLine="false"
      barWidth="28%"
    />

    <div class="px-5 mt-4">
      <div v-for="item in totalItems" :key="item.label" class="flex items-center mb-5 last:mb-0">
        <div class="flex items-center justify-start w-3/5 text-sm">
          <div
            class="w-10 h-10 mr-3 text-lg rounded-md flex items-center justify-center"
            :class="item.iconClass"
          >
            <FaSvgIcon :icon="item.icon" />
          </div>

          <div class="flex flex-col items-start">
            <span class="text-base text-g-800">{{ item.label }}</span>
            <span class="mt-1 text-xs text-g-500">{{ item.subLabel }}</span>
          </div>
        </div>
        <div class="text-lg font-normal" :class="item.valueClass">{{ item.value }}</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface UsageSeries {
  name: string;
  data: number[];
}

const weekDays = ref(["周一", "周二", "周三", "周四", "周五", "周六", "周日"]);

/** 本周每日实际功能调用 */
const usageData = ref<UsageSeries[]>([
  {
    name: "代码生成",
    data: [48, 52, 36, 61, 44, 22, 18],
  },
]);

const totalItems = [
  {
    icon: "ri:code-s-slash-line",
    iconClass: "text-theme bg-theme/12",
    label: "实际生成",
    subLabel: "本周",
    value: "281",
    valueClass: "text-theme",
  },
  {
    icon: "ri:flag-line",
    iconClass: "text-theme bg-theme/12",
    label: "计划生成",
    subLabel: "本周",
    value: "320",
    valueClass: "text-theme",
  },
];
</script>
