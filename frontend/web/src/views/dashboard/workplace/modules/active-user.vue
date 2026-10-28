<template>
  <div class="fa-card h-105 p-4 box-border">
    <FaBarChart
      class="box-border p-2"
      barWidth="50%"
      height="13.7rem"
      :showAxisLine="false"
      :data="chartData"
      :xAxisData="xAxisLabels"
    />
    <div class="ml-1">
      <h3 class="mt-5 text-lg font-medium">构建概览</h3>
      <p class="mt-1 text-sm">
        比上周
        <span class="text-success font-medium">+6.2%</span>
      </p>
      <p class="mt-1 text-sm">汇总编译、打包与构建的月度执行情况</p>
    </div>
    <div class="flex justify-between mt-2">
      <div class="flex-1" v-for="item in list" :key="item.name">
        <p class="text-2xl text-g-900">{{ item.num }}</p>
        <p class="text-xs text-g-500">{{ item.name }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface UserStatItem {
  name: string;
  num: string;
}

// 最近9个月
const xAxisLabels = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月"];

// 每月构建次数
const chartData = [72, 80, 68, 90, 86, 78, 94, 88, 96];

/** 构建概览指标 */
const list: UserStatItem[] = [
  { name: "本月构建", num: "412" },
  { name: "成功率", num: "89%" },
  { name: "平均耗时", num: "8.4分" },
  { name: "周环比", num: "+6.2%" },
];
</script>
