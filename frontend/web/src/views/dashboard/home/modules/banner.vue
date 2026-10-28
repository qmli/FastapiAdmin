<template>
  <ElCarousel height="220px" :interval="6000">
    <ElCarouselItem v-for="slide in slides" :key="slide.title">
      <a class="solution-slide" :href="slide.href" target="_blank" rel="noopener noreferrer">
        <img class="solution-slide__image" :src="slide.image" :alt="slide.title" />
        <div class="solution-slide__content">
          <p class="solution-slide__title">{{ slide.title }}</p>
          <p class="solution-slide__subtitle">{{ slide.subtitle }}</p>
          <span class="solution-slide__button">查看详情</span>
        </div>
      </a>
    </ElCarouselItem>
  </ElCarousel>
</template>

<script setup lang="ts">
import vehicleBanner from "@imgs/isoft/vehicle-banner.jpg";
import vehicleTest from "@imgs/isoft/vehicle-test.jpg";
import vehicleEcu from "@imgs/isoft/vehicle-ecu.jpg";
import vehicleCpap from "@imgs/isoft/vehicle-cpap.jpg";

const SITE = "https://www.i-soft.com.cn";

const slides = [
  {
    title: "车用基础软件解决方案",
    subtitle: "面向智能网联汽车感知、决策与控制系统的基础软件方案。",
    image: vehicleBanner,
    href: `${SITE}/solution/vehicle.html`,
  },
  {
    title: "汽车电子测试开发解决方案",
    subtitle: "覆盖软件代码测试、整车网络开发与测试、控制单元功能测试。",
    image: vehicleTest,
    href: `${SITE}/solution/vehicle-test-development.html`,
  },
  {
    title: "ECU软硬件一体化解决方案",
    subtitle: "遵循 V 型开发流程，满足整车控制器及中央网关控制器量产需求。",
    image: vehicleEcu,
    href: `${SITE}/solution/vehicle-ECU.html`,
  },
  {
    title: "普华汽车开放系统架构整车软件解决方案",
    subtitle: "硬实时、高安全、低能耗，支持传统汽车向智能网联汽车发展。",
    image: vehicleCpap,
    href: `${SITE}/solution/vehicle-CPAP.html`,
  },
];
</script>

<style lang="scss" scoped>
.solution-slide {
  position: relative;
  display: block;
  height: 100%;
  overflow: hidden;
  color: #fff;
  text-decoration: none;
  border-radius: calc(var(--custom-radius) + 2px);

  &__image {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }

  &__content {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-width: 68%;
    padding: 0 2rem;
    background: linear-gradient(90deg, rgb(8 28 72 / 72%) 0%, rgb(8 28 72 / 18%) 78%, transparent 100%);
  }

  &__title {
    margin: 0 0 0.5rem;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.35;
  }

  &__subtitle {
    margin: 0 0 1.25rem;
    font-size: 0.9rem;
    line-height: 1.5;
    opacity: 0.92;
  }

  &__button {
    box-sizing: border-box;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: fit-content;
    min-width: 80px;
    height: var(--el-component-custom-height);
    padding: 0 12px;
    font-size: 14px;
    color: #333;
    background: #fff;
    border-radius: 6px;
  }
}

@media (width <= 640px) {
  .solution-slide {
    &__content {
      max-width: 100%;
      padding: 16px;
      background: linear-gradient(180deg, rgb(8 28 72 / 20%) 0%, rgb(8 28 72 / 72%) 100%);
      justify-content: flex-end;
    }

    &__title {
      font-size: 1.15rem;
    }

    &__subtitle {
      display: -webkit-box;
      margin-bottom: 0.75rem;
      overflow: hidden;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
    }
  }
}
</style>
