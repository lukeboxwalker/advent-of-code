
<h1>Day 5: If You Give A Seed A Fertilizer 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2023/day/5>Link to Day 5</a><h2>Part One 🎁</h2><p>You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.</p>
<p>"A water source? Island Island <b>is</b> the water source!" You point out that Snow Island isn't receiving any water.</p>
<p>"Oh, we had to stop the water because we <b>ran out of sand</b> to <a href="https://en.wikipedia.org/wiki/Sand_filter" target="_blank">filter</a> it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.</p>
<p>"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"</p>
<p>You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our <b>food production problem</b>. The latest Island Island <a href="https://en.wikipedia.org/wiki/Almanac" target="_blank">Almanac</a> just arrived and we're having trouble making sense of it."</p>
<p>The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil <code>123</code> and fertilizer <code>123</code> aren't necessarily related to each other.</p>
<p>For example:</p>
<pre><code>seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
</code></pre>
<p>The almanac starts by listing which seeds need to be planted: seeds <code>79</code>, <code>14</code>, <code>55</code>, and <code>13</code>.</p>
<p>The rest of the almanac contains a list of <b>maps</b> which describe how to convert numbers from a <b>source category</b> into numbers in a <b>destination category</b>. That is, the section that starts with <code>seed-to-soil map:</code> describes how to convert a <b>seed number</b> (the source) to a <b>soil number</b> (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.</p>
<p>Rather than list every source number and its corresponding destination number one by one, the maps describe entire <b>ranges</b> of numbers that can be converted. Each line within a map contains <span title="Don't blame me for the weird order. Blame LXC container.conf UID mappings.">three numbers</span>: the <b>destination range start</b>, the <b>source range start</b>, and the <b>range length</b>.</p>
<p>Consider again the example <code>seed-to-soil map</code>:</p>
<pre><code>50 98 2
52 50 48
</code></pre>
<p>The first line has a <b>destination range start</b> of <code>50</code>, a <b>source range start</b> of <code>98</code>, and a <b>range length</b> of <code>2</code>. This line means that the source range starts at <code>98</code> and contains two values: <code>98</code> and <code>99</code>. The destination range is the same length, but it starts at <code>50</code>, so its two values are <code>50</code> and <code>51</code>. With this information, you know that seed number <code>98</code> corresponds to soil number <code>50</code> and that seed number <code>99</code> corresponds to soil number <code>51</code>.</p>
<p>The second line means that the source range starts at <code>50</code> and contains <code>48</code> values: <code>50</code>, <code>51</code>, ..., <code>96</code>, <code>97</code>. This corresponds to a destination range starting at <code>52</code> and also containing <code>48</code> values: <code>52</code>, <code>53</code>, ..., <code>98</code>, <code>99</code>. So, seed number <code>53</code> corresponds to soil number <code>55</code>.</p>
<p>Any source numbers that <b>aren't mapped</b> correspond to the <b>same</b> destination number. So, seed number <code>10</code> corresponds to soil number <code>10</code>.</p>
<p>So, the entire list of seed numbers and their corresponding soil numbers looks like this:</p>
<pre><code>seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
</code></pre>
<p>With this map, you can look up the soil number required for each initial seed number:</p>
<ul>
<li>Seed number <code>79</code> corresponds to soil number <code>81</code>.</li>
<li>Seed number <code>14</code> corresponds to soil number <code>14</code>.</li>
<li>Seed number <code>55</code> corresponds to soil number <code>57</code>.</li>
<li>Seed number <code>13</code> corresponds to soil number <code>13</code>.</li>
</ul>
<p>The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find <b>the lowest location number that corresponds to any of the initial seeds</b>. To do this, you'll need to convert each seed number through other categories until you can find its corresponding <b>location number</b>. In this example, the corresponding types are:</p>
<ul>
<li>Seed <code>79</code>, soil <code>81</code>, fertilizer <code>81</code>, water <code>81</code>, light <code>74</code>, temperature <code>78</code>, humidity <code>78</code>, <b>location <code>82</code></b>.</li>
<li>Seed <code>14</code>, soil <code>14</code>, fertilizer <code>53</code>, water <code>49</code>, light <code>42</code>, temperature <code>42</code>, humidity <code>43</code>, <b>location <code>43</code></b>.</li>
<li>Seed <code>55</code>, soil <code>57</code>, fertilizer <code>57</code>, water <code>53</code>, light <code>46</code>, temperature <code>82</code>, humidity <code>82</code>, <b>location <code>86</code></b>.</li>
<li>Seed <code>13</code>, soil <code>13</code>, fertilizer <code>52</code>, water <code>41</code>, light <code>34</code>, temperature <code>34</code>, humidity <code>35</code>, <b>location <code>35</code></b>.</li>
</ul>
<p>So, the lowest location number in this example is <code><b>35</b></code>.</p>
<p><b>What is the lowest location number that corresponds to any of the initial seed numbers?</b></p>

<p>To begin, <a href="5/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="5/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22If+You+Give+A+Seed+A+Fertilizer%22+%2D+Day+5+%2D+Advent+of+Code+2023&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F5&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=%22If+You+Give+A+Seed+A+Fertilizer%22+%2D+Day+5+%2D+Advent+of+Code+2023+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F5';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
