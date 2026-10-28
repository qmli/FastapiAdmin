<template>
  <div class="fa-card h-82 p-5 mb-5 max-sm:mb-4 flex flex-col">
    <div class="fa-card-header">
      <div class="title">
        <h4>功能使用趋势</h4>
        <p>BSW 配置与代码生成</p>
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

const xAxisData = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"];

/** 全年各月的 BSW 配置与代码生成次数 */
const chartData = computed<LineDataItem[]>(() => [
  {
    name: "BSW 配置",
    data: [120, 132, 128, 140, 150, 148, 160, 172, 168, 180, 176, 186],
  },
  {
    name: "代码生成",
    data: [60, 64, 58, 70, 72, 68, 80, 84, 78, 88, 90, 96],
  },
]);
</script>
