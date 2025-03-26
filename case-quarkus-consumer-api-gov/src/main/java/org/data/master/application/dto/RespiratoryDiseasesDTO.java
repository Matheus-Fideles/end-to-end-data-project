package org.data.master.application.dto;

import java.util.List;

import org.data.master.application.domain.model.RespiratoryDiseases;

public record RespiratoryDiseasesDTO( List<RespiratoryDiseases> respiratoryDiseaseses, Pagination pagination) {
    
}
