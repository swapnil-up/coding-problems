package Kyu5

import kotlin.math.abs


@OptIn(ExperimentalStdlibApi::class)
fun rgb(r: Int, g: Int, b: Int): String {
    var red= if (r<0) 0 else r
    var green=if (g<0) 0 else g
    var blue=if (b<0) 0 else b
    if (red>255) red=255
    if (blue>255) blue=255
    if (green>255) green=255
    var res=red.toString(16).let { if (it.length==1) "0$it" else it }+green.toString(16).let { if (it.length==1) "0$it" else it }+blue.toString(16).let { if (it.length==1) "0$it" else it }
    return res.uppercase()
}

//var res=red.toHexString().substring(6)+blue.toHexString().substring(6)+green.toHexString().substring(6)

fun main() {
    println(rgb(0, 0, 0))
    println(rgb(0, 0, -20))
    println(rgb(300,255,255))
    println(rgb(173,255,47))
    println(rgb(148, 0, 211))
}