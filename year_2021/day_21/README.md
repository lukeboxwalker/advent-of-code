

<h1>Day 21: Dirac Dice 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2021/day/21>Link to Day 21</a><h2>Part One 🎁</h2><p>There's not much to do as you slowly descend to the bottom of the ocean. The submarine computer <span title="A STRANGE GAME.">challenges you to a nice game</span> of <b>Dirac Dice</b>.</p>
<p>This game consists of a single <a href="https://en.wikipedia.org/wiki/Dice" target="_blank">die</a>, two <a href="https://en.wikipedia.org/wiki/Glossary_of_board_games#piece" target="_blank">pawns</a>, and a game board with a circular track containing ten spaces marked <code>1</code> through <code>10</code> clockwise. Each player's <b>starting space</b> is chosen randomly (your puzzle input). Player 1 goes first.</p>
<p>Players take turns moving. On each player's turn, the player rolls the die <b>three times</b> and adds up the results. Then, the player moves their pawn that many times <b>forward</b> around the track (that is, moving clockwise on spaces in order of increasing value, wrapping back around to <code>1</code> after <code>10</code>). So, if a player is on space <code>7</code> and they roll <code>2</code>, <code>2</code>, and <code>1</code>, they would move forward 5 times, to spaces <code>8</code>, <code>9</code>, <code>10</code>, <code>1</code>, and finally stopping on <code>2</code>.</p>
<p>After each player moves, they increase their <b>score</b> by the value of the space their pawn stopped on. Players' scores start at <code>0</code>. So, if the first player starts on space <code>7</code> and rolls a total of <code>5</code>, they would stop on space <code>2</code> and add <code>2</code> to their score (for a total score of <code>2</code>). The game immediately ends as a win for any player whose score reaches <b>at least <code>1000</code></b>.</p>
<p>Since the first game is a practice game, the submarine opens a compartment labeled <b>deterministic dice</b> and a 100-sided die falls out. This die always rolls <code>1</code> first, then <code>2</code>, then <code>3</code>, and so on up to <code>100</code>, after which it starts over at <code>1</code> again. Play using this die.</p>
<p>For example, given these starting positions:</p>
<pre><code>Player 1 starting position: 4
Player 2 starting position: 8
</code></pre>
<p>This is how the game would go:</p>
<ul>
<li>Player 1 rolls <code>1</code>+<code>2</code>+<code>3</code> and moves to space <code>10</code> for a total score of <code>10</code>.</li>
<li>Player 2 rolls <code>4</code>+<code>5</code>+<code>6</code> and moves to space <code>3</code> for a total score of <code>3</code>.</li>
<li>Player 1 rolls <code>7</code>+<code>8</code>+<code>9</code> and moves to space <code>4</code> for a total score of <code>14</code>.</li>
<li>Player 2 rolls <code>10</code>+<code>11</code>+<code>12</code> and moves to space <code>6</code> for a total score of <code>9</code>.</li>
<li>Player 1 rolls <code>13</code>+<code>14</code>+<code>15</code> and moves to space <code>6</code> for a total score of <code>20</code>.</li>
<li>Player 2 rolls <code>16</code>+<code>17</code>+<code>18</code> and moves to space <code>7</code> for a total score of <code>16</code>.</li>
<li>Player 1 rolls <code>19</code>+<code>20</code>+<code>21</code> and moves to space <code>6</code> for a total score of <code>26</code>.</li>
<li>Player 2 rolls <code>22</code>+<code>23</code>+<code>24</code> and moves to space <code>6</code> for a total score of <code>22</code>.</li>
</ul>
<p>...after many turns...</p>
<ul>
<li>Player 2 rolls <code>82</code>+<code>83</code>+<code>84</code> and moves to space <code>6</code> for a total score of <code>742</code>.</li>
<li>Player 1 rolls <code>85</code>+<code>86</code>+<code>87</code> and moves to space <code>4</code> for a total score of <code>990</code>.</li>
<li>Player 2 rolls <code>88</code>+<code>89</code>+<code>90</code> and moves to space <code>3</code> for a total score of <code>745</code>.</li>
<li>Player 1 rolls <code>91</code>+<code>92</code>+<code>93</code> and moves to space <code>10</code> for a final score, <code>1000</code>.</li>
</ul>
<p>Since player 1 has at least <code>1000</code> points, player 1 wins and the game ends. At this point, the losing player had <code>745</code> points and the die had been rolled a total of <code>993</code> times; <code>745 * 993 = <b>739785</b></code>.</p>
<p>Play a practice game using the deterministic 100-sided die. The moment either player wins, <b>what do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?</b></p>

<p>To begin, <a href="21/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="21/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22Dirac+Dice%22+%2D+Day+21+%2D+Advent+of+Code+2021&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2021%2Fday%2F21&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' && mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=%22Dirac+Dice%22+%2D+Day+21+%2D+Advent+of+Code+2021+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2021%2Fday%2F21'}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
