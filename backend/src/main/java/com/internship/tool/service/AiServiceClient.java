package com.internship.tool.service;

import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;

import java.util.Map;

@Component
public class AiServiceClient {

    private final RestTemplate restTemplate = new RestTemplate();
    private static final String BASE_URL = "http://localhost:5000";

    public Object generateReport(Map<String, Object> request) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, Object>> entity = new HttpEntity<>(request, headers);

            ResponseEntity<Object> response = restTemplate.postForEntity(
                    BASE_URL + "/generate-report",
                    entity,
                    Object.class
            );

            return response.getBody();

        } catch (Exception e) {
            return null;
        }
    }
}