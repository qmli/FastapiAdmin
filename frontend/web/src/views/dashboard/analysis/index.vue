<template>
  <div>
    <ElRow :gutter="20">
      <ElCol :xl="14" :lg="15" :xs="24"><TodaySales /></ElCol>
      <ElCol :xl="10" :lg="9" :xs="24"><VisitorInsights /></ElCol>
    </ElRow>

    <ElRow :gutter="20">
      <ElCol :xl="12" :lg="12" :xs="24" class="flex flex-col gap-5">
        <CustomerSatisfaction class="flex-1" />
        <TotalRevenue class="flex-1" />
      </ElCol>
      <ElCol :xl="12" :lg="12" :xs="24" class="flex flex-col gap-5">
        <TargetVsReality class="flex-1" />
        <TopProducts class="flex-1" />
      </ElCol>
    </ElRow>

    <ElRow :gutter="20">
      <ElCol :xl="12" :lg="12" :xs="24"><SalesMappingByCountry /></ElCol>
      <ElCol :xl="12" :lg="12" :xs="24"><VolumeServiceLevel /></ElCol>
    </ElRow>
  </div>
</template>

<script setup lang="ts">
import TodaySales from "./modules/today-sales.vue";
import VisitorInsights from "./modules/visitor-insights.vue";
import TotalRevenue from "./modules/total-revenue.vue";
import CustomerSatisfaction from "./modules/customer-satisfaction.vue";
import TargetVsReality from "./modules/target-vs-reality.vue";
import TopProducts from "./modules/top-products.vue";
import SalesMappingByCountry from "./modules/sales-mapping-by-country.vue";
import VolumeServiceLevel from "./modules/volume-service-level.vue";

defineOptions({ name: "DashboardAnalysis" });
</script>

<style scoped>
:deep(.el-card) {
  --el-card-border-radius: calc(var(--custom-radius) + 2px);

  border: 1px solid var(--fa-card-border);
}
</style>
