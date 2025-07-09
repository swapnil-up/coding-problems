package Kyu7

fun nbYear(pp0:Int, percent:Double, aug:Int, p:Int):Int {
    var d=percent/100
    var nbYear:Int=0
    var newP:Int=pp0
    while (newP<p){
        newP= (newP+d*newP+aug).toInt()
        nbYear+=1
    }
    return(nbYear)
}

fun main() {
    var nbYear:Int= nbYear(1500, 5.0, 100, 5000)
    println("$nbYear")
//    testing(nbYear(1500000, 2.5, 10000, 2000000), 10)

    }

