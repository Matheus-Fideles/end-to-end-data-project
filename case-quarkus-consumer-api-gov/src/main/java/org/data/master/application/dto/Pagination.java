package org.data.master.application.dto;

public record Pagination(Integer currentPage, Integer size, Long totalPages, Long totalRecords) {
    
}
