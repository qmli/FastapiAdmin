<template>
  <div class="fa-card h-82 p-5 mb-5 overflow-hidden max-lg:h-auto max-sm:mb-4">
    <div class="fa-card-header pr-0">
      <div class="title">
        <h4>今日使用</h4>
        <p>AUTOSAR 配置与生成</p>
      </div>
      <div
        class="flex items-center justify-center h-7.5 min-w-17 border border-g-300 rounded-lg text-g-500 cursor-pointer"
      >
        <FaSvgIcon icon="ri:arrow-up-line" class="text-base mr-1.5" />
        <span class="text-xs">导出</span>
      </div>
    </div>

    <div class="mt-2">
      <ElRow :gutter="20">
        <ElCol :span="6" :xs="24" v-for="item in usageData" :key="item.label">
          <div
            class="flex px-5 flex-col justify-center h-55 border border-g-300/85 rounded-xl max-lg:mb-4 max-sm:flex-row max-sm:justify-between max-sm:items-center max-sm:h-40"
          >
            <div class="size-12 rounded-lg flex items-center justify-center bg-theme/10">
              <FaSvgIcon :icon="item.icon" class="text-xl text-theme" />
            </div>

            <div class="max-sm:ml-4 mt-3.5 max-sm:mt-0 max-sm:text-end">
              <FaCountTo class="text-2xl font-medium" :target="item.value" :duration="1500" />
              <p class="mt-2 text-base text-g-600 max-sm:mt-1">{{ item.label }}</p>
              <small class="text-g-500 mt-1 max-sm:mt-0.5">
                较昨天
                <span
                  class="font-medium"
                  :class="[item.change.indexOf('+') === -1 ? 'text-danger' : 'text-success']"
                >
                  {{ item.change }}
                </span>
              </small>
            </div>
          </div>
        </ElCol>
      </ElRow>
    </div>
  </div>
</template>

<script setup lang="ts">
interface UsageDataItem {
  label: string;
  value: number;
  change: string;
  icon: string;
}

/** 今日 AUTOSAR 工具功能使用 */
const usageData = ref<UsageDataItem[]>([
  {
    label: "BSW 配置",
    value: 86,
    change: "+8%",
    icon: "ri:settings-3-line",
  },
  {
    label: "SWC 设计",
    value: 42,
    change: "+6%",
    icon: "ri:node-tree",
  },
  {
    label: "RTE 生成",
    value: 24,
    change: "+11%",
    icon: "ri:code-s-slash-line",
  },
  {
    label: "配置校验",
    value: 31,
    change: "-4%",
    icon: "ri:checkbox-circle-line",
  },
]);
</script>
