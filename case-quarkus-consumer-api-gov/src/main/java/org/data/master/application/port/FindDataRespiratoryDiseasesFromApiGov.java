package org.data.master.application.port;

import java.util.List;

import org.data.master.application.domain.model.RespiratoryDiseases;

public interface FindDataRespiratoryDiseasesFromApiGov {
    
    List<RespiratoryDiseases> execute(Integer year);
}
