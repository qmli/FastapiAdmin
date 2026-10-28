<template>
  <div class="fa-card h-100 p-5 mb-5 max-sm:mb-4">
    <div class="fa-card-header">
      <div class="title">
        <h4>热门功能</h4>
        <p>AUTOSAR 配置与生成</p>
      </div>
    </div>
    <ElScrollbar class="h-full">
      <FaTable
        :data="features"
        :style="{ width: '100%' }"
        size="large"
        :border="false"
        :stripe="false"
        :header-cell-style="{ background: 'transparent' }"
      >
        <ElTableColumn type="index" label="序号" width="60" />
        <ElTableColumn prop="name" label="功能" min-width="120" />
        <ElTableColumn prop="share" label="占比">
          <template #default="scope">
            <ElProgress
              :percentage="scope.row.share"
              :color="getColor(scope.row.share)"
              :stroke-width="5"
              :show-text="false"
            />
          </template>
        </ElTableColumn>
        <ElTableColumn prop="calls" label="次数" width="80">
          <template #default="scope">
            <span
              :style="{
                color: getColor(scope.row.share),
                backgroundColor: `rgba(${hexToRgb(getColor(scope.row.share))}, 0.08)`,
                border: '1px solid',
                padding: '3px 6px',
                borderRadius: '4px',
                fontSize: '12px',
              }"
            >
              {{ scope.row.calls }}
            </span>
          </template>
        </ElTableColumn>
      </FaTable>
    </ElScrollbar>
  </div>
</template>

<script setup lang="ts">
import { hexToRgb } from "@utils";

interface FeatureUsage {
  name: string;
  share: number;
  calls: string;
}

const COLOR_THRESHOLDS = {
  LOW: 25,
  MEDIUM: 50,
  HIGH: 75,
} as const;

const POPULARITY_COLORS = {
  LOW: "#00E096",
  MEDIUM: "#0095FF",
  HIGH: "#884CFF",
  VERY_HIGH: "#FE8F0E",
} as const;

/** AUTOSAR 工具功能使用排行 */
const features = computed<FeatureUsage[]>(() => [
  { name: "BSW 模块配置", share: 92, calls: "412" },
  { name: "RTE 生成", share: 74, calls: "186" },
  { name: "通信栈配置", share: 61, calls: "130" },
  { name: "诊断服务配置", share: 48, calls: "96" },
  { name: "SWC 端口设计", share: 36, calls: "64" },
  { name: "ARXML 导入", share: 28, calls: "48" },
]);

const getColor = (percentage: number): string => {
  if (percentage < COLOR_THRESHOLDS.LOW) return POPULARITY_COLORS.LOW;
  if (percentage < COLOR_THRESHOLDS.MEDIUM) return POPULARITY_COLORS.MEDIUM;
  if (percentage < COLOR_THRESHOLDS.HIGH) return POPULARITY_COLORS.HIGH;
  return POPULARITY_COLORS.VERY_HIGH;
};
</script>
