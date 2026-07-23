package Kyu7

fun highAndLow(numbers: String): String {
    var a=numbers.split(" ")
    var max:Int=a[0].toInt()
    var min:Int=a[0].toInt()
    for(i in 0 .. a.count()-1){
        if (max<a[i].toInt()) max=a[i].toInt()
        if(min>a[i].toInt()) min=a[i].toInt()
    }
    return (max.toString()+" "+min.toString())
}

fun main() {
    println(highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
    println(highAndLow("1 2 3"))
}
