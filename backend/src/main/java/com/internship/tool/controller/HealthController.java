package com.internship.tool.controller;

import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/health")
public class HealthController {

    private static final long startTime = System.currentTimeMillis();
    private static long totalResponseTime = 0;
    private static int requestCount = 0;

    public static void recordResponseTime(long time) {
        totalResponseTime += time;
        requestCount++;
    }

    @GetMapping
    public Map<String, Object> health() {

        long uptime = System.currentTimeMillis() - startTime;
        long avgResponse = requestCount == 0 ? 0 : totalResponseTime / requestCount;

        Map<String, Object> data = new HashMap<>();
        data.put("model", "Groq LLM");
        data.put("uptime_ms", uptime);
        data.put("avg_response_time_ms", avgResponse);

        return data;
    }
}