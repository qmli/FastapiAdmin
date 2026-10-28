<template>
  <div class="fa-card h-82 p-5 mb-5 max-sm:mb-4">
    <div class="fa-card-header">
      <div class="title">
        <h4>模块使用</h4>
        <p>BSW 模块的配置次数与使用人数</p>
      </div>
    </div>

    <FaBarChart
      class="mt-6"
      height="14.3rem"
      :data="volumeServiceData"
      :xAxisData="serviceCategories"
      :showLegend="true"
      :showAxisLine="false"
      :stack="false"
      barWidth="22%"
    />
  </div>
</template>

<script setup lang="ts">
interface VolumeServiceDataItem {
  name: string;
  data: number[];
  stack: string;
}

/**
 * Classic AUTOSAR 常用 BSW 模块
 */
const serviceCategories = ref(["CAN", "Ethernet", "诊断", "NvM", "RTE"]);

/**
 * 各模块的配置次数与使用人数
 */
const volumeServiceData = ref<VolumeServiceDataItem[]>([
  {
    name: "配置",
    data: [168, 96, 124, 72, 142],
    stack: "total",
  },
  {
    name: "用户",
    data: [32, 18, 26, 14, 29],
    stack: "total",
  },
]);
</script>
