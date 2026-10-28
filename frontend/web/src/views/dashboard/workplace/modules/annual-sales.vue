<template>
  <div class="fa-card p-5 h-112">
    <div class="fa-card-header">
      <div class="title">
        <h4>年度构建</h4>
        <p>按季度统计</p>
      </div>
    </div>

    <FaBarChart
      :showAxisLabel="false"
      :showAxisLine="false"
      :showSplitLine="false"
      :data="[86, 92, 78, 110]"
      barWidth="26px"
      height="calc(100% - 155px)"
    />
    <div class="flex justify-around mt-10">
      <div class="flex items-center">
        <div
          class="flex items-center justify-center size-10.5 mr-2.5 text-theme bg-theme/10 rounded-lg"
        >
          <FaSvgIcon icon="ri:code-s-slash-line" class="text-xl" />
        </div>
        <div>
          <p class="text-lg">1,286</p>
          <span class="text-sm">编译</span>
        </div>
      </div>
      <div class="flex items-center">
        <div
          class="flex items-center justify-center size-10.5 mr-2.5 text-theme bg-theme/10 rounded-lg"
        >
          <FaSvgIcon icon="ri:archive-line" class="text-xl" />
        </div>
        <div>
          <p class="text-lg">428</p>
          <span class="text-sm">打包</span>
        </div>
      </div>
    </div>
  </div>
</template>
