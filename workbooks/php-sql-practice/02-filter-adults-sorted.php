<?php

// Write filterAdults(array $users): array that returns full user arrays
// of users 18+, sorted by age ascending. Tiebreak alphabetically by name.

function filterAdults(array $users): array {
    $adults = [];
    foreach ($users as $user) {
        if ($user['age'] >= 18) {
            $adults[] = $user;
        }
    }
    usort($adults, function ($a, $b) {
        return [$a['age'], $a['name']] <=> [$b['age'], $b['name']];
    });
    return $adults;
}

$users = [
    ['name' => 'Bob', 'age' => 22],
    ['name' => 'Alice', 'age' => 22],
    ['name' => 'Charlie', 'age' => 17],
];

print_r(filterAdults($users));
//
// Problem: Filter users 18+, return full arrays sorted by age ascending,
//          tiebreak alphabetically by name.
//
// Why: Tests foreach, array building, AND custom sorting with usort().
//
// Key lessons:
//   - sort() on arrays-of-arrays is unreliable — use usort() with a callback
//   - PHP's <=> (spaceship) operator returns -1, 0, or 1
//   - [$a['age'], $a['name']] <=> [$b['age'], $b['name']] compares
//     element-by-element — first age, then name as tiebreaker
//   - usort() modifies the array in place, returns bool
