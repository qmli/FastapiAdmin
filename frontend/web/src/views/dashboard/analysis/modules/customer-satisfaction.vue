<template>
  <div class="fa-card h-100 p-5 mb-5 max-sm:mb-4 flex flex-col">
    <div class="fa-card-header">
      <div class="title">
        <h4>功能完成率</h4>
        <p>配置校验通过的比例</p>
      </div>
    </div>
    <FaLineChart
      class="flex-1 min-h-0"
      :data="chartData"
      :xAxisData="xAxisData"
      :showLegend="true"
      :showAxisLabel="true"
      :showAxisLine="false"
      :showSplitLine="true"
    />
  </div>
</template>

<script setup lang="ts">
import type { LineDataItem } from "@/types/component/chart";

const AREA_STYLE_CONFIG = {
  startOpacity: 0.08,
  endOpacity: 0,
} as const;

const xAxisData = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"];

/** 功能完成率，对比上月与本月 */
const chartData = computed<LineDataItem[]>(() => [
  {
    name: "上月",
    data: [82, 84, 83, 85, 86, 84, 85],
    areaStyle: AREA_STYLE_CONFIG,
  },
  {
    name: "本月",
    data: [86, 87, 88, 89, 90, 88, 89],
    areaStyle: AREA_STYLE_CONFIG,
  },
]);
</script>
