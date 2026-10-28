<template>
  <div class="fa-card h-100 p-5 mb-5 max-sm:mb-4 flex flex-col">
    <div class="fa-card-header">
      <div class="title">
        <h4>本周配置</h4>
        <p>通信、诊断与 RTE</p>
      </div>
    </div>
    <FaBarChart
      class="flex-1 min-h-0"
      :data="usageData"
      :xAxisData="weekDays"
      :showLegend="true"
      :showAxisLine="false"
      barWidth="18%"
    />
  </div>
</template>

<script setup lang="ts">
interface UsageSeries {
  name: string;
  data: number[];
}

const weekDays = ref(["周一", "周二", "周三", "周四", "周五", "周六", "周日"]);

/** 本周通信、诊断与 RTE 的每日配置次数 */
const usageData = ref<UsageSeries[]>([
  {
    name: "通信",
    data: [48, 52, 36, 61, 55, 22, 18],
  },
  {
    name: "诊断",
    data: [22, 18, 14, 28, 24, 8, 6],
  },
  {
    name: "RTE",
    data: [30, 28, 22, 36, 32, 12, 8],
  },
]);
</script>
