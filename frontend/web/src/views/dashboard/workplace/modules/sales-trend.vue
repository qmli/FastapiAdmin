<template>
  <div class="fa-card p-5 h-112">
    <div class="fa-card-header">
      <div class="title">
        <h4>构建结果</h4>
        <p>成功与失败对比</p>
      </div>
    </div>

    <FaDualBarCompareChart
      :positiveData="[72, 80, 68, 90, 86]"
      :negativeData="[8, 12, 10, 6, 14]"
      positiveName="成功"
      negativeName="失败"
      :xAxisData="['六月', '七月', '八月', '九月', '十月']"
      height="19rem"
    />
  </div>
</template>
