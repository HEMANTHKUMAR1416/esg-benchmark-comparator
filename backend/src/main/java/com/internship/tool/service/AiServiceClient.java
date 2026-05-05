package com.internship.tool.service;

import com.internship.tool.controller.HealthController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.http.*;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.security.MessageDigest;
import java.util.Map;
import java.util.concurrent.TimeUnit;

@Component
public class AiServiceClient {

    private static final String BASE_URL = "http://localhost:5000";

    @Autowired
    private RestTemplate restTemplate;

    @Autowired
    private StringRedisTemplate redisTemplate;

    public Object generateReport(Map<String, Object> request) {

        String key = generateKey(request.toString());

        // 🔥 CACHE CHECK
        String cached = redisTemplate.opsForValue().get(key);
        if (cached != null) {
            System.out.println("✅ CACHE HIT");
            return cached;
        }

        try {
            long start = System.currentTimeMillis();

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, Object>> entity = new HttpEntity<>(request, headers);

            ResponseEntity<String> response = restTemplate.postForEntity(
                    BASE_URL + "/generate-report",
                    entity,
                    String.class
            );

            long end = System.currentTimeMillis();

            // ⏱ Track time
            HealthController.recordResponseTime(end - start);

            String result = response.getBody();

            // 🔥 SAVE CACHE (15 min)
            redisTemplate.opsForValue().set(
                    key,
                    result,
                    15,
                    TimeUnit.MINUTES
            );

            return result;

        } catch (Exception e) {
            System.out.println("AI ERROR: " + e.getMessage());
            return null;
        }
    }

    // 🔐 SHA256 KEY
    private String generateKey(String input) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(input.getBytes());
            StringBuilder hex = new StringBuilder();

            for (byte b : hash) {
                hex.append(String.format("%02x", b));
            }

            return hex.toString();

        } catch (Exception e) {
            return input;
        }
    }
}