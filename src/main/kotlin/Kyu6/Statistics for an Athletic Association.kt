package Kyu6

import kotlin.math.round

object Stat {

    fun stat(s: String): String {
        var pieces=s.split(", ","|")
        var n=pieces.count()
        var values= IntArray(n/3)
        for (i in 0..n-1 step(3)){
            values[i/3]+=(pieces[i].toInt()*3600+pieces[i+1].toInt()*60+pieces[i+2].toInt())
        }
        values.forEach { println(it) }
        values.sort()
        var range=values.last().toInt()-values.first().toInt()
        var mean=values.sumOf { it.toInt() }/values.size
        var median=if (values.size%2==0) (values[values.size/2].toInt()+values[values.size/2+1].toInt())/2
                    else values[(values.size/2).toInt()]
        return ("Range: "+formatting(range)+" Average: "+ formatting(mean)+" Median: "+ formatting(median))
    }
    fun formatting(seconds:Int):String{
        val hours=seconds/3600
        val min=(seconds%3600)/60
        val second=seconds%60
        return String.format("%02d|%02d|%02d",hours,min,second)
    }

}


fun main() {
    println(Stat.stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
    println(Stat.stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"))

}