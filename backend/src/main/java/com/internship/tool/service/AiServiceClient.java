package com.internship.tool.service;

import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;

import java.util.Map;

@Component
public class AiServiceClient {

    private final RestTemplate restTemplate = new RestTemplate();

    private static final String BASE_URL = "http://localhost:5000";

    public String getDescription(Map<String, Object> request) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, Object>> entity = new HttpEntity<>(request, headers);

            ResponseEntity<Map> response = restTemplate.postForEntity(
                    BASE_URL + "/describe",
                    entity,
                    Map.class
            );

            return response.getBody().get("summary").toString();

        } catch (Exception e) {
            return null;
        }
    }

    public Object getRecommendations(Map<String, Object> request) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, Object>> entity = new HttpEntity<>(request, headers);

            ResponseEntity<Map> response = restTemplate.postForEntity(
                    BASE_URL + "/recommend",
                    entity,
                    Map.class
            );

            return response.getBody().get("recommendations");

        } catch (Exception e) {
            return null;
        }
    }
}