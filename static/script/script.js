Shery.mouseFollower();
Shery.makeMagnet(".magnet", {
    //Parameters are optional.
    ease: "cubic-bezier(0.23, 1, 0.320, 1)",
    duration: 1,
  });


  Shery.textAnimate(".mainanimation", {
    //Parameters are optional.
    style: 1,
    y: 10,
    delay: 0.1,
    duration: 5,
    ease: "cubic-bezier(0.23, 1, 0.320, 1)",
    multiplier: 0.1,
  });

  Shery.hoverWithMediaCircle(".hvr" /* Element to target.*/, {
    // images: ["/img/melody.jpg"] /*OR*/,
    videos: ["static/videos/vid.mp4"],
  });