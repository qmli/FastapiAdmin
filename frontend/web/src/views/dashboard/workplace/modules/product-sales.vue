<template>
  <div class="fa-card h-53 p-5 pt-3.5">
    <div class="fa-card-header">
      <div class="title">
        <h4 class="text-2xl">
          <span>186</span>
          <FaSvgIcon icon="ri:arrow-right-up-line" class="text-success text-lg ml-1" />
        </h4>
        <p>编译次数</p>
      </div>
    </div>

    <FaBarChart
      :showAxisLabel="false"
      :showAxisLine="false"
      :showSplitLine="false"
      :data="[18, 22, 19, 25, 21, 28, 36]"
      barWidth="16px"
      height="5.6rem"
    />
  </div>
</template>
