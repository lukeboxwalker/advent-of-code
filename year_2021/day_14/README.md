

<h1>Day 14: Extended Polymerization 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2021/day/14>Link to Day 14</a><h2>Part One 🎁</h2><p>The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has <a href="https://en.wikipedia.org/wiki/Polymerization" target="_blank">polymerization</a> equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.</p>
<p>The submarine manual contains <span title="HO&#xa;&#xa;HO -&gt; OH">instructions</span> for finding the optimal polymer formula; specifically, it offers a <b>polymer template</b> and a list of <b>pair insertion</b> rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.</p>
<p>For example:</p>
<pre><code>NNCB

CH -&gt; B
HH -&gt; N
CB -&gt; H
NH -&gt; C
HB -&gt; C
HC -&gt; B
HN -&gt; C
NN -&gt; C
BH -&gt; H
NC -&gt; B
NB -&gt; B
BN -&gt; B
BB -&gt; N
BC -&gt; B
CC -&gt; N
CN -&gt; C
</code></pre>
<p>The first line is the <b>polymer template</b> - this is the starting point of the process.</p>
<p>The following section defines the <b>pair insertion</b> rules. A rule like <code>AB -&gt; C</code> means that when elements <code>A</code> and <code>B</code> are immediately adjacent, element <code>C</code> should be inserted between them. These insertions all happen simultaneously.</p>
<p>So, starting with the polymer template <code>NNCB</code>, the first step simultaneously considers all three pairs:</p>
<ul>
<li>The first pair (<code>NN</code>) matches the rule <code>NN -&gt; C</code>, so element <code><b>C</b></code> is inserted between the first <code>N</code> and the second <code>N</code>.</li>
<li>The second pair (<code>NC</code>) matches the rule <code>NC -&gt; B</code>, so element <code><b>B</b></code> is inserted between the <code>N</code> and the <code>C</code>.</li>
<li>The third pair (<code>CB</code>) matches the rule <code>CB -&gt; H</code>, so element <code><b>H</b></code> is inserted between the <code>C</code> and the <code>B</code>.</li>
</ul>
<p>Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.</p>
<p>After the first step of this process, the polymer becomes <code>N<b>C</b>N<b>B</b>C<b>H</b>B</code>.</p>
<p>Here are the results of a few steps using the above rules:</p>
<pre><code>Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
</code></pre>
<p>This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, <code>B</code> occurs 1749 times, <code>C</code> occurs 298 times, <code>H</code> occurs 161 times, and <code>N</code> occurs 865 times; taking the quantity of the most common element (<code>B</code>, 1749) and subtracting the quantity of the least common element (<code>H</code>, 161) produces <code>1749 - 161 = <b>1588</b></code>.</p>
<p>Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. <b>What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?</b></p>

<h2>Part Two 🎁</h2><p>The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of <b>40 steps</b> should do it.</p>
<p>In the above example, the most common element is <code>B</code> (occurring <code>2192039569602</code> times) and the least common element is <code>H</code> (occurring <code>3849876073</code> times); subtracting these produces <code><b>2188189693529</b></code>.</p>
<p>Apply <b>40</b> steps of pair insertion to the polymer template and find the most and least common elements in the result. <b>What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?</b></p>

