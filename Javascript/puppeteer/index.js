const puppeteer = require('puppeteer');

const fetchYoutubeChannelData = async (channelURL) => {
  // launching the CHROMIUM Browser
  const browser = await puppeteer.launch({ headless: true });
  try {
    // opening the new blank tab
    const page = await browser.newPage();
    console.log('wait...');

    // navigating to the Channel in the 2nd new tab
    await page.goto(channelURL);

    // Channel Name
    const [channelNameElement] = await page.$x(
      '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string'
    );
    const text = await channelNameElement.getProperty('textContent');
    const channelName = await text.jsonValue();

    // Subscribers
    const [subscribersElement] = await page.$x('//*[@id="subscriber-count"]');
    const textSubscribers = await subscribersElement.getProperty('textContent');
    const subscribers = await textSubscribers.jsonValue();

    // Channel Avatar
    const [channelAvatarElement] = await page.$x(
      '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/yt-img-shadow/img'
    );
    const imageSrc = await channelAvatarElement.getProperty('src');
    const channelAvatar = await imageSrc.jsonValue();

    console.log({ channelName, subscribers, channelAvatar });
  } catch (error) {
    console.log(error.message);
  } finally {
    // at last closing the browser
    await browser.close();
  }
};

fetchYoutubeChannelData(
  'https://www.youtube.com/channel/UCLyLELCANeaMvOFdzyNHTOw'
);

/*
{
  channelName: 'coding bakht',
  subscribers: '138 subscribers',
  channelAvatar: 'https://yt3.ggpht.com/IYSACJR0GJKJop9b5Q-zFGlvomcYznJgV_nBpmNxYQNEzWn4DvlZA0wJscdPPAH2_VaU9vFGMg=s88-c-k-c0x00ffffff-no-rj'
}
*/
