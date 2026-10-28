<template>
  <ElCarousel height="400px">
    <ElCarouselItem>
      <FaCardBanner
        title="构建环境正常"
        description="编译节点与制品库连接正常，当前没有阻塞中的构建。"
      />
    </ElCarouselItem>

    <ElCarouselItem>
      <FaCardBanner
        :image="icon2"
        title="失败构建待处理"
        description="今日有 4 个构建失败，建议优先重试基础软件编译。"
        :button="{
          show: true,
          text: '查看构建',
          color: 'var(--fa-warning)',
          textColor: '#fff',
        }"
        @click="handleViewBuilds"
      />
    </ElCarouselItem>

    <ElCarouselItem>
      <FaCardBanner
        :image="icon3"
        title="本周构建摘要"
        description="近 7 日完成 128 次构建，成功率 87.5%。"
        :button="{
          show: true,
          text: '知道了',
          color: 'var(--fa-error)',
          textColor: '#fff',
        }"
        @click="handleSummary"
      />
    </ElCarouselItem>

    <ElCarouselItem>
      <FaCardBanner
        :image="icon4"
        title="工具链版本更新"
        description="交叉编译工具链 3.1.0 已可用于新的打包任务。"
        :button="{
          show: true,
          text: '知道了',
          color: 'var(--theme-color)',
          textColor: '#fff',
        }"
        :cancelButton="{
          show: true,
          text: '稍后处理',
          color: '#eee',
          textColor: '#333',
        }"
        @click="handleConfirm"
        @cancel="handleCancel"
      />
    </ElCarouselItem>
  </ElCarousel>
</template>

<script setup lang="ts">
// 非关键组件异步导入（延迟加载，提升首屏速度）
import { ElMessage } from "element-plus";
import FaCardBanner from "@/components/banners/fa-card-banner/index.vue";
import icon2 from "@imgs/3d/icon2.webp";
import icon3 from "@imgs/3d/icon3.webp";
import icon4 from "@imgs/3d/icon4.webp";

defineOptions({ name: "ItBanners" });

const handleViewBuilds = () => {
  ElMessage.info("构建记录将在任务模块接入后打开");
};

const handleSummary = () => {
  ElMessage.success("本周构建摘要已阅");
};

const handleConfirm = () => {
  ElMessage.success("已记录工具链 3.1.0");
};

const handleCancel = () => {
  ElMessage.info("已稍后处理");
};
</script>
