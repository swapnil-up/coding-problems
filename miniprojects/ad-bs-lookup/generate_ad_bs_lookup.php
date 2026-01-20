#!/usr/bin/env php
<?php

/**
 * Standalone AD-BS Date Lookup Generator
 * Generates a lookup table for converting between AD and BS (Bikram Sambat) dates
 * 
 * Usage: php generate_ad_bs_lookup.php [--from=1944-01-01] [--to=2033-12-31] [--chunk=500]
 */

class AdBsLookupGenerator
{
    private $pdo;
    private $_bs = [
        0  => [2000, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        1  => [2001, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        2  => [2002, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        3  => [2003, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        4  => [2004, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        5  => [2005, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        6  => [2006, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        7  => [2007, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        8  => [2008, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
        9  => [2009, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        10 => [2010, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        11 => [2011, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        12 => [2012, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        13 => [2013, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        14 => [2014, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        15 => [2015, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        16 => [2016, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        17 => [2017, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        18 => [2018, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        19 => [2019, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        20 => [2020, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        21 => [2021, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        22 => [2022, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        23 => [2023, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        24 => [2024, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        25 => [2025, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        26 => [2026, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        27 => [2027, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        28 => [2028, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        29 => [2029, 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30],
        30 => [2030, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        31 => [2031, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        32 => [2032, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        33 => [2033, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        34 => [2034, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        35 => [2035, 30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
        36 => [2036, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        37 => [2037, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        38 => [2038, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        39 => [2039, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        40 => [2040, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        41 => [2041, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        42 => [2042, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        43 => [2043, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        44 => [2044, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        45 => [2045, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        46 => [2046, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        47 => [2047, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        48 => [2048, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        49 => [2049, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        50 => [2050, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        51 => [2051, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        52 => [2052, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        53 => [2053, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        54 => [2054, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        55 => [2055, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        56 => [2056, 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30],
        57 => [2057, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        58 => [2058, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        59 => [2059, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        60 => [2060, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        61 => [2061, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        62 => [2062, 30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31],
        63 => [2063, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        64 => [2064, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        65 => [2065, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        66 => [2066, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
        67 => [2067, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        68 => [2068, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        69 => [2069, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        70 => [2070, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        71 => [2071, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        72 => [2072, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        73 => [2073, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        74 => [2074, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        75 => [2075, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        76 => [2076, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        77 => [2077, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        78 => [2078, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        79 => [2079, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        80 => [2080, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        81 => [2081, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        82 => [2082, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        83 => [2083, 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],// all bullshit from here
        84 => [2084, 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],
        85 => [2085, 31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30],
        86 => [2086, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        87 => [2087, 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30],
        88 => [2088, 30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30],
        89 => [2089, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        90 => [2090, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
    ];

    public function __construct()
    {
        $this->loadEnv();
        $this->connectDatabase();
    }

    /**
     * Load .env file
     */
    private function loadEnv()
    {
        $envPath = __DIR__ . '/.env';
        
        if (!file_exists($envPath)) {
            die("Error: .env file not found at {$envPath}\n");
        }

        $lines = file($envPath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        foreach ($lines as $line) {
            // Skip comments
            if (strpos(trim($line), '#') === 0) {
                continue;
            }

            // Parse KEY=VALUE
            if (strpos($line, '=') !== false) {
                list($key, $value) = explode('=', $line, 2);
                $key = trim($key);
                $value = trim($value);
                
                // Remove quotes if present
                $value = trim($value, '"\'');
                
                if (!array_key_exists($key, $_ENV)) {
                    $_ENV[$key] = $value;
                    putenv("{$key}={$value}");
                }
            }
        }
    }

    /**
     * Connect to database using .env credentials
     */
    private function connectDatabase()
    {
        $host = getenv('DB_HOST') ?: 'localhost';
        $port = getenv('DB_PORT') ?: '3306';
        $database = getenv('DB_DATABASE');
        $username = getenv('DB_USERNAME');
        $password = getenv('DB_PASSWORD');

        if (!$database || !$username) {
            die("Error: DB_DATABASE and DB_USERNAME must be set in .env file\n");
        }

        try {
            $dsn = "mysql:host={$host};port={$port};dbname={$database};charset=utf8mb4";
            $this->pdo = new PDO($dsn, $username, $password, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            ]);
            echo "✓ Connected to database: {$database}\n";
        } catch (PDOException $e) {
            die("Database connection failed: " . $e->getMessage() . "\n");
        }
    }

    /**
     * Run the generator
     */
    public function run($options)
    {
        $from = new DateTime($options['from'] ?? '1944-01-01');
        $to = new DateTime($options['to'] ?? '2033-12-31');
        $chunkSize = (int)($options['chunk'] ?? 500);

        echo "Generating AD↔BS lookup from {$from->format('Y-m-d')} to {$to->format('Y-m-d')}...\n";

        // Create table
        $this->pdo->exec("
            CREATE TABLE IF NOT EXISTS ad_bs_lookup (
                ad_date VARCHAR(10) PRIMARY KEY,
                bs_date VARCHAR(10) NOT NULL
            )
        ");
        echo "✓ Table created/verified\n";

        $current = clone $from;
        $rows = [];
        $inserted = 0;

        while ($current <= $to) {
            $ad = $current->format('Y-m-d');
            $bs = $this->eng_to_nep(
                (int)$current->format('Y'),
                (int)$current->format('m'),
                (int)$current->format('d')
            );
            $bsDate = "{$bs['year']}-{$bs['month']}-{$bs['date']}";

            $rows[] = [
                'ad_date' => $ad,
                'bs_date' => $bsDate,
            ];

            if (count($rows) >= $chunkSize) {
                $this->insertBatch($rows);
                $inserted += count($rows);
                echo "\rInserted: {$inserted}";
                $rows = [];
            }

            $current->modify('+1 day');
        }

        // Insert remaining rows
        if (!empty($rows)) {
            $this->insertBatch($rows);
            $inserted += count($rows);
        }

        echo "\n✓ Done! Inserted/updated total: {$inserted} rows.\n";
    }

    /**
     * Insert batch of rows
     */
    private function insertBatch($rows)
    {
        $values = array_map(function ($row) {
            return "('{$row['ad_date']}', '{$row['bs_date']}')";
        }, $rows);

        $sql = "INSERT INTO ad_bs_lookup (ad_date, bs_date) VALUES " . implode(',', $values) . 
               " ON DUPLICATE KEY UPDATE bs_date = VALUES(bs_date)";
        
        $this->pdo->exec($sql);
    }

    /**
     * Check if date is in valid range.
     */
    private function _is_in_range_eng($yy, $mm, $dd)
    {
        if ($yy < 1944 || $yy > 2033) {
            return 'Supported only between 1944-2033';
        }
        if ($mm < 1 || $mm > 12) {
            return 'Error! month value can be between 1-12 only';
        }
        if ($dd < 1 || $dd > 31) {
            return 'Error! day value can be between 1-31 only';
        }
        return true;
    }

    /**
     * Check if english year is leap year.
     */
    private function is_leap_year($year)
    {
        return ($year % 400 == 0) || ($year % 4 == 0 && $year % 100 != 0);
    }

    /**
     * Convert English date to Nepali date (AD 1944-2033).
     */
    private function eng_to_nep($yy, $mm, $dd)
    {
        $chk = $this->_is_in_range_eng($yy, $mm, $dd);
        if ($chk !== true) {
            die($chk);
        }

        $month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        $lmonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        
        $def_eyy = 1944;
        $def_nyy = 2000;
        $def_nmm = 9;
        $def_ndd = 16;
        
        $total_eDays = 0;

        // Count total days from base year
        for ($i = 0; $i < ($yy - $def_eyy); $i++) {
            $daysInYear = $this->is_leap_year($def_eyy + $i) ? $lmonth : $month;
            for ($j = 0; $j < 12; $j++) {
                $total_eDays += $daysInYear[$j];
            }
        }

        // Add days from months in current year
        for ($i = 0; $i < ($mm - 1); $i++) {
            $total_eDays += $this->is_leap_year($yy) ? $lmonth[$i] : $month[$i];
        }

        // Add remaining days
        $total_eDays += $dd;

        // Convert to Nepali date
        $i = 0;
        $j = $def_nmm;
        $total_nDays = $def_ndd;
        $m = $def_nmm;
        $y = $def_nyy;

        while ($total_eDays != 0) {
            $a = $this->_bs[$i][$j];
            $total_nDays++;

            if ($total_nDays > $a) {
                $m++;
                $total_nDays = 1;
                $j++;
            }

            if ($m > 12) {
                $y++;
                $m = 1;
            }

            if ($j > 12) {
                $j = 1;
                $i++;
            }

            $total_eDays--;
        }

        return [
            'year' => $y,
            'month' => $m < 10 ? '0' . $m : $m,
            'date' => $total_nDays < 10 ? '0' . $total_nDays : $total_nDays
        ];
    }
}

// Parse command line arguments
$options = getopt('', ['from:', 'to:', 'chunk:']);

// Run the generator
try {
    $generator = new AdBsLookupGenerator();
    $generator->run($options);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
    exit(1);
}