<template>
  <div class="root">
    <!-- Your HTML content goes here -->

    <div class="leonbox">The answer is in the folders you will find...</div>
    <div class="userblue"></div>
    <div class="newblue"></div>
    <div class="userbox">Where do I find the information on Vue?</div>
    <div class="newbox">Ask me anything!</div>
    <div class="vector">
      <img class="icon2" src="@/assets/clip.png" alt="Clip" />
    </div>

    <div class="bCHAi">BCHAI</div>
    <div class="mascot"></div>
    <div class="profile"></div>
  </div>
</template>

<script>
export default {
  name: "MyComponent",
};
</script>

<style scoped>
/* The CSS you provided, scoped to this component */
.root {
  position: relative;
  width: 1440px;
  height: 1024px;
  flex-direction: column;
  align-items: flex-start;
  background-color: #fff;
  overflow: hidden;
}

.ellipse2 {
  position: absolute;
  left: 462px;
  top: 78px;
  width: 102px;
  height: 95px;
  overflow: visible;
}

.icon {
  width: 100%;
  height: 100%;
}

.leonbox {
  color: #043258;
  font-size: 16px;
  font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif;
  position: absolute;
  left: 527px;
  top: 313px;
  width: 368px;
  height: 39px;
  flex-direction: column;
}

.userblue {
  position: absolute;
  left: 445px;
  top: 871px;
  width: 550px;
  height: 57px;
  border-radius: 20px;
  background-color: #d4f2ff;
}

.newblue {
  position: absolute;
  left: 590px;
  top: 173px;
  width: 405px;
  height: 81px;
  border-radius: 20px;
  background-color: #d4f2ff;
}

.userbox {
  color: #043258;
  font-size: 16px;
  font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif;
  position: absolute;
  left: 616px;
  top: 194px;
  width: 368px;
  height: 39px;
  flex-direction: column;
}

.newbox {
  color: #043258;
  font-size: 16px;
  font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif;
  position: absolute;
  left: 516px;
  top: 889px;
  width: 323px;
  height: 39px;
  flex-direction: column;
}

.vector {
  position: absolute;
  left: 32.0833%;
  right: 65.5556%;
  top: 86.6211%;
  bottom: 11.2305%;
  overflow: visible;
}

.icon2 {
  width: 100%;
  height: 100%;
}

.ellipse1 {
  position: absolute;
  left: 462px;
  top: 309px;
  width: 46px;
  height: 46px;
  overflow: visible;
}

.icon3 {
  width: 100%;
  height: 100%;
}

.bCHAi {
  color: #043258;
  font-size: 28px;
  font-weight: 500;
  font-family: Roboto, system-ui, -apple-system, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif;
  position: absolute;
  left: 551px;
  top: 105px;
  width: 338px;
  height: 58px;
  flex-direction: column;
}

.mascot {
  position: absolute;
  left: 469px;
  top: 312px;
  width: 32px;
  height: 40px;
  border-radius: 10px;
  background-image: url("@/assets/mascot.png"); /* Use @ to reference src/assets */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.profile {
  position: absolute;
  left: 454px;
  top: 66px;
  width: 96px;
  height: 103px;
  background-image: url("@/assets/profile.png"); /* Use @ to reference src/assets */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
