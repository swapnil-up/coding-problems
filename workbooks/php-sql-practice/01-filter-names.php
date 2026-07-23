<?php

function processUsers(array $users): array {
    $names = [];
    foreach ($users as $user) {
        if ($user['age'] >= 18) {
            $names[] = $user['name'];
        }
    }
    sort($names);
    return $names;
}

$users = [
    ['name' => 'Bob', 'age' => 22],
    ['name' => 'Alice', 'age' => 17],
    ['name' => 'Charlie', 'age' => 19],
];

print_r(processUsers($users));

//
// Problem: Filter users 18+ and return their names sorted alphabetically.
//
// Why: Tests foreach iteration, associative array access ($user['age']),
//      array building with $names[], and sort() — all fundamental PHP.
//
// Key syntax lessons:
//   - foreach ($array as $element) not "for (i in $array)"
//   - Array keys need quotes: $user['age'] not $user[age]
//   - Array push: $array[] = $value (no .push() method)
//   - sort() is a function that modifies in place, not a method
//   - Always use {} for control structures and ; to end statements
