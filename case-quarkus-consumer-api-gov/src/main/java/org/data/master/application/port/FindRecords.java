package org.data.master.application.port;

import org.data.master.application.dto.RespiratoryDiseasesDTO;

public interface FindRecords {
    
    RespiratoryDiseasesDTO execute(Integer year, Integer month, Integer page, Integer size);
}
