<template>
  <div class="fa-card h-105 p-5">
    <div class="fa-card-header">
      <div class="title">
        <h4>构建趋势</h4>
        <p>
          今年增长
          <span class="text-success">+8.6%</span>
        </p>
      </div>
    </div>
    <FaLineChart
      height="calc(100% - 56px)"
      :data="data"
      :xAxisData="xAxisData"
      :showAreaColor="true"
      :showAxisLine="false"
    />
  </div>
</template>

<script setup lang="ts">
/**
 * 全年构建次数
 */
const data = [62, 58, 70, 66, 74, 72, 80, 68, 90, 86, 78, 94];

/**
 * X 轴月份标签
 */
const xAxisData = [
  "1月",
  "2月",
  "3月",
  "4月",
  "5月",
  "6月",
  "7月",
  "8月",
  "9月",
  "10月",
  "11月",
  "12月",
];
</script>
