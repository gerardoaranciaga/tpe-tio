<?php
//FUNCIONES PARA ARMAR EL GRAFO----------------------
function agregarNodo(&$grafo, $ID){
    if (!array_key_exists($ID, $grafo)){
        $grafo[$ID] = array();
        return true;
    }
    return false;

}

function existeNodo($grafo, $ID){
    return array_key_exists($ID, $grafo);
}

function agregarArco(&$grafo, $desde, $hasta, $costo){
    if (array_key_exists($desde, $grafo) && array_key_exists($hasta, $grafo)){
        $grafo[$desde][$hasta] = $costo;
        return true;
    }
    return false;
    
}

function existeArco($grafo, $desde, $hasta){
    return isset($grafo[$desde][$hasta]);
}

function costoArco($grafo, $desde, $hasta){
    return $grafo[$desde][$hasta];
}
//---------------------------------------------------
//PRIM
////
function arc_min_peso($V,$S,$grafo){
    $m = INF;    
    $diff = array_diff($V, $S);
    $u = -1;
    $v = -1;
    foreach ($S as $s){
        foreach ($diff as $d){
            if (existeArco($grafo, $s, $d) && costoArco($grafo, $s, $d) < $m){
                $m = costoArco($grafo, $s, $d);
                $u = $s;
                $v = $d;
            }
        }
    }
    return [$u, $v];
}

function prim($grafo){
	$A = array();
	$V = array_keys($grafo);	
	$u = $V[0];		
	$S = array();
	$S[] = $u;	
	while (( count( $S ) != count( $V ))){
        $arco = arc_min_peso($V,$S,$grafo);	
		print_r($arco);
        $A[] = $arco;
        $S[] = $arco[1];	
	}
}

$grafo = array();
////
agregarNodo($grafo, 1);
agregarNodo($grafo, 2);
agregarNodo($grafo, 3);
agregarNodo($grafo, 4);
agregarNodo($grafo, 5);
agregarNodo($grafo, 6);
//////
agregarArco($grafo, 1, 2, 10);
agregarArco($grafo, 1, 5, 45);
agregarArco($grafo, 1, 4, 30);
agregarArco($grafo, 2, 1, 10);
agregarArco($grafo, 2, 5, 40);
agregarArco($grafo, 2, 6, 25);
agregarArco($grafo, 2, 3, 50);
agregarArco($grafo, 3, 2, 50);
agregarArco($grafo, 3, 5, 35);
agregarArco($grafo, 3, 6, 15);
agregarArco($grafo, 4, 1, 30);
agregarArco($grafo, 4, 6, 20);
agregarArco($grafo, 5, 1, 45);
agregarArco($grafo, 5, 2, 40);
agregarArco($grafo, 5, 6, 55);
agregarArco($grafo, 5, 3, 35);
agregarArco($grafo, 6, 4, 20);
agregarArco($grafo, 6, 5, 55);
agregarArco($grafo, 6, 2, 25);
agregarArco($grafo, 6, 3, 15);
////
prim($grafo);

/* CAMBIO 1 PARA COLABORAR EN GIT */
/* CAMBIO 2 PARA COLABORAR EN GIT */