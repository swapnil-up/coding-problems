package Kyu6

import java.lang.Math.pow

object ASum {
    fun findNb(m: Long): Long {
        var c:Long=-1
        var size:Long=1
        var n=1
        while(size<m){
            n+=1
            size=(((pow(n.toDouble(),2.0))*pow((n+1).toDouble(),2.0))/4).toLong()
            if(size==m) c=n.toLong()
        }
        return(c)
    }
}

fun main(){

        println(ASum.findNb(56396345062501))
        println(ASum.findNb(6132680780625))
//        testing(28080884739601, -1)
}