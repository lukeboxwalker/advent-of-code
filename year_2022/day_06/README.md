
<h1>Day 6: Tuning Trouble 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2022/day/6>Link to Day 6</a><h2>Part One 🎁</h2><p>The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the <b>star</b> fruit grove.</p>
<p>As you move through the dense undergrowth, one of the Elves gives you a handheld <b>device</b>. He says that it has many fancy features, but the most important one to set up right now is the <b>communication system</b>.</p>
<p>However, because he's heard you have <a href="/2016/day/6">significant</a> <a href="/2016/day/25">experience</a> <a href="/2019/day/7">dealing</a> <a href="/2019/day/9">with</a> <a href="/2019/day/16">signal-based</a> <a href="/2021/day/25">systems</a>, he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.</p>
<p>As if inspired by comedic timing, the device emits a few <span title="The magic smoke, on the other hand, seems to be contained... FOR NOW!">colorful sparks</span>.</p>
<p>To be able to communicate with the Elves, the device needs to <b>lock on to their signal</b>. The signal is a series of seemingly-random characters that the device receives one at a time.</p>
<p>To fix the communication system, you need to add a subroutine to the device that detects a <b>start-of-packet marker</b> in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of <b>four characters that are all different</b>.</p>
<p>The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.</p>
<p>For example, suppose you receive the following datastream buffer:</p>
<pre><code>mjqjpqmgbljsphdztnvjfqwrcgsmlb</code></pre>
<p>After the first three characters (<code>mjq</code>) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters <code>mjqj</code>. Because <code>j</code> is repeated, this isn't a marker.</p>
<p>The first time a marker appears is after the <b>seventh</b> character arrives. Once it does, the last four characters received are <code>jpqm</code>, which are all different. In this case, your subroutine should report the value <code><b>7</b></code>, because the first start-of-packet marker is complete after 7 characters have been processed.</p>
<p>Here are a few more examples:</p>
<ul>
<li><code>bvwbjplbgvbhsrlpgdmjqwftvncz</code>: first marker after character <code><b>5</b></code></li>
<li><code>nppdvjthqldpwncqszvftbrmjlhg</code>: first marker after character <code><b>6</b></code></li>
<li><code>nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg</code>: first marker after character <code><b>10</b></code></li>
<li><code>zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw</code>: first marker after character <code><b>11</b></code></li>
</ul>
<p><b>How many characters need to be processed before the first start-of-packet marker is detected?</b></p>

<p>To begin, <a href="6/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="6/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22Tuning+Trouble%22+%2D+Day+6+%2D+Advent+of+Code+2022&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F6&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' && mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=%22Tuning+Trouble%22+%2D+Day+6+%2D+Advent+of+Code+2022+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F6'}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
