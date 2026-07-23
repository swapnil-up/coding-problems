<?php

// ============================================================
// EDGE CASE: Why sort() fails on arrays of arrays
// ============================================================

$users = [
    ['name' => 'Bob',   'age' => 22],
    ['name' => 'Zara',  'age' => 19],  // younger but Z > B
    ['name' => 'Alice', 'age' => 22],
];

// WRONG — sort() compares arrays by their first key (name), not by age
$wrong = [];
foreach ($users as $u) { if ($u['age'] >= 18) $wrong[] = $u; }
sort($wrong);
print_r($wrong);
// Bob (22) first because B < Z < A — age 19 Zara ends up in middle

echo "\n--- vs usort() ---\n";

// RIGHT — usort() with spaceship compares by age, then name
$right = [];
foreach ($users as $u) { if ($u['age'] >= 18) $right[] = $u; }
usort($right, function ($a, $b) {
    return [$a['age'], $a['name']] <=> [$b['age'], $b['name']];
});
print_r($right);
// Zara (19), Alice (22), Bob (22)

//
// ============================================================
// THEORY RECAP
// ============================================================
//
// 1. foreach ($array as $element)
//    - Loops over each element; $array is NOT modified
//    - Use foreach ($array as $key => $value) if you need the key
//    - No "for (i in array)" — that's Python/JS, not PHP
//
// 2. $adults[] = $user
//    - Appends $user to the end of $adults array
//    - Equivalent to array_push($adults, $user) but faster (no function call)
//    - [] is the "array push operator"
//
// 3. usort(array, callable)
//    - Sorts array IN PLACE (no return value, modifies original)
//    - Callback takes two elements $a, $b from the array
//    - Must return: negative if $a < $b, 0 if equal, positive if $a > $b
//    - Callback is a "closure" (anonymous function)
//
// 4. Spaceship operator <=>
//    - Returns -1, 0, or 1
//    - $a <=> $b means: compare $a vs $b
//    - Works on strings, numbers, arrays — even mixed types
//    - Arrays compare element-by-element: first key, then second, etc.
//
// 5. [$a['age'], $a['name']] <=> [$b['age'], $b['name']]
//    - Builds a temporary array for comparison
//    - PHP compares first element (age), then second (name) if ages equal
//    - This is a PHP idiom — concise multi-criteria sort
//
// 6. Closures (anonymous functions)
//    - function ($params) use ($outerVars) { ... }
//    - No "use" needed here because we only use $a, $b passed by usort
//    - Closures capture variables from the outer scope when "use" is specified
//