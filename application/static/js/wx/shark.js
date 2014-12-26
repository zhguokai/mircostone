// DeviceOrientation将底层的方向传感器和运动传感器进行了高级封装，提供了DOM事件的支持。
// 这个特性包括两个事件：
// 1、deviceOrientation：封装了方向传感器数据的事件，可以获取手机静止状态下的方向数据（手机所处的角度、方位和朝向等）。
// 2、deviceMotion：封装了运动传感器的事件，可以获取手机运动状态下的运动加速度等数据。
// 使用这两个事件，可以很能够实现重力感应、指南针等有趣的功能。

// 现在在很多Native应用中有一个非常常见而时尚的功能 —— 摇一摇，摇一摇找人、摇一摇看新闻、摇一摇找金币。。。
// 也许在android或者ios的客户端上对这个功能你已经很了解了，但是现在，我将告诉你如何在手机网页上实现摇一摇的功能。

// OK，那我们现在就开始吧，嘿嘿~
// 先来让我们了解一下设备运动事件 —— DeviceMotionEvent:返回设备关于加速度和旋转的相关信息，其中加速度的数据包含以下三个方向：
// x：横向贯穿手机屏幕；
// y：纵向贯穿手机屏幕；
// z：垂直手机屏幕。
// 鉴于有些设备没有排除重力的影响，所以该事件会返回两个属性：
// 1、accelerationIncludingGravity(含重力的加速度)
// 2、acceleration(排除重力影响的加速度)

// 作为码农，上代码才是最直接的，come on，代码走起！

// 首先在页面上要监听运动传感事件


// 那么，我们如何计算用户是否是在摇动手机呢？可以从以下几点进行考虑：
// 1、其实用户在摇动手机的时候始终都是以一个方向为主进行摇动的；
// 2、用户在摇动手机的时候在x、y、z三个方向都会有相应的想速度的变化；
// 3、不能把用户正常的手机运动行为当做摇一摇（手机放在兜里，走路的时候也会有加速度的变化）。
// 从以上三点考虑，针对三个方向上的加速度进行计算，间隔测量他们，考察他们在固定时间段里的变化率，而且需要确定一个阀值来触发摇一摇之后的操作。

// 首先，定义一个摇动的阀值
var SHAKE_THRESHOLD = 1000;
// 定义一个变量保存上次更新的时间
var last_update = 0;
// 紧接着定义x、y、z记录三个轴的数据以及上一次出发的时间
var x = 0;
var y = 0;
var z = 0;
var last_x = 0;
var last_y = 0;
var last_z = 0;
var length = 0;
//定义事件捕捉器
function deviceMotionHandler(eventData) {
    // 获取含重力的加速度
    var acceleration = eventData.accelerationIncludingGravity;
    // 获取当前时间
    var curTime = new Date().getTime();
    var diffTime = curTime - last_update;
    // 固定时间段
    if (diffTime > 150) {
        //console.log("dddddd");1
        //摇晃开始播放声音
        last_update = curTime;
        x = acceleration.x;
        y = acceleration.y;
        z = acceleration.z;
         var speed = Math.abs(x + y + z - last_x - last_y - last_z) / diffTime * 15000;
        length += Math.abs(x + y + z - last_x - last_y - last_z) / 3;
       // var speed = Math.abs(z - last_z) / diffTime * 15000;
        //length += Math.abs(z - last_z);
        //使晃动的时间长一些
        if (speed > SHAKE_THRESHOLD && length > 100) {
            length = 0;
            //window.remove1EventListener('devicemotion', deviceMotionHandler);
            // TODO:在此处可以实现摇一摇之后所要进行的数据逻辑操作
            //记录源音频地址,播放摇一摇音频
            //$("#yyRing")[0].play();
            //为了播放完音乐，延时1秒钟提交
            setTimeout("subData()", 1500);
            return;
        }

        last_x = x;
        last_y = y;
        last_z = z;

    }
}

//提交方法
var subData = function () {
   // $("#yyRing")[0].pause();
    $("#wxcqForm")[0].submit();
}
