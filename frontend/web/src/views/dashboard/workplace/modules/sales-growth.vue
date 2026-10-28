<template>
  <div class="fa-card h-53 p-5 pt-3.5">
    <div class="fa-card-header">
      <div class="title">
        <h4 class="text-2xl">
          <span>89%</span>
          <FaSvgIcon icon="ri:arrow-right-up-line" class="text-success text-lg ml-1" />
        </h4>
        <p>构建成功率</p>
      </div>
    </div>

    <FaLineChart
      :showAreaColor="true"
      :showAxisLabel="false"
      :showAxisLine="false"
      :showSplitLine="false"
      :data="[82, 84, 83, 86, 87, 88, 89]"
      barWidth="16px"
      height="5rem"
    />
  </div>
</template>
