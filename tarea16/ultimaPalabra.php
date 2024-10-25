<?php
    function ultimaPalabra($arreglo){
        $n=strlen($arreglo);
        $subArreglo=array();
        $k=0; #Iterador para subArreglo
        for($i=$n-1; $i>=0 ;$i--){
            if($arreglo[$i]!=" "){
                $subArreglo[$k]=$arreglo[$i];
                $k=$k+1;
            }else{
                break;
            }
        }
        $cad="";
        for($i=$k-1;$i>=0;$i--){
            $cad.=$subArreglo[$i];//Concatenacion
        }
        return $cad;
    }
//Prueba:
$cadena="Hola Mundo";
echo (ultimaPalabra($cadena));
?>