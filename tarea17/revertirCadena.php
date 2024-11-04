<?php
function revertirVocales($s) {
    $v = ["a" => "a", "e" => "e", "i" => "i",
        "o" => "o", "u" => "u", "A" => "A", "E" => "E",
        "I" => "I", "O" => "O", "U" => "U"];

    $i = 0;
    $j = strlen($s) - 1;

    while ($i < $j) {
        if (!array_key_exists($s[$i], $v)) {
            $i++;
        } elseif (!array_key_exists($s[$j], $v)) {
            $j--;
        } else {
            $aux = $s[$i];
            $s[$i] = $s[$j];
            $s[$j] = $aux;
            $i++;
            $j--;
        }
    }
    return $s;
}

echo revertirVocales("lapiz") . "\n";
echo revertirVocales("Icecream") . "\n";
?>