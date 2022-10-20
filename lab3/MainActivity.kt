package com.example.cse118lab3

import android.app.Activity
import android.net.wifi.WifiManager
import android.os.Bundle
import com.example.cse118lab3.databinding.ActivityMainBinding


class MainActivity : Activity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // isProviderEnabled(LocationManager.GPS_PROVIDER)
        val latitude;
        val longitude;
        // getCurrentLocation(1)


        val wifiInfo = context.getSystemService(WIFI_SERVICE).connectionInfo
        val rssi = wifiInfo.rssi
        val level = WifiManager.calculateSignalLevel(wifiInfo.rssi, 5)
        println("RSSI is $level dBm");
        println("Level is $level out of 5");
    }
}