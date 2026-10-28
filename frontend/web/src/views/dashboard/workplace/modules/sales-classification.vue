<template>
  <div class="fa-card p-5 h-112">
    <div class="fa-card-header">
      <div class="title">
        <h4>任务分布</h4>
        <p>按编译、打包、构建</p>
      </div>
    </div>

    <FaRingChart
      :data="[
        { value: 186, name: '编译' },
        { value: 96, name: '打包' },
        { value: 130, name: '构建' },
      ]"
      :color="['#4C87F3', '#EDF2FF', '#8BD8FC']"
      :radius="['70%', '80%']"
      height="16.5rem"
      :showLabel="false"
      :borderRadius="0"
      centerText="412"
    />
    <div class="flex justify-around">
      <div class="flex items-center">
        <div
          class="flex items-center justify-center size-10.5 mr-2.5 text-theme bg-theme/10 rounded-lg"
        >
          <FaSvgIcon icon="ri:checkbox-circle-line" class="text-xl" />
        </div>
        <div>
          <p class="text-lg">368</p>
          <span class="text-sm">成功</span>
        </div>
      </div>
      <div class="flex items-center">
        <div
          class="flex items-center justify-center size-10.5 mr-2.5 text-theme bg-theme/10 rounded-lg"
        >
          <FaSvgIcon icon="ri:close-circle-line" class="text-xl" />
        </div>
        <div>
          <p class="text-lg">28</p>
          <span class="text-sm">失败</span>
        </div>
      </div>
    </div>
  </div>
</template>
